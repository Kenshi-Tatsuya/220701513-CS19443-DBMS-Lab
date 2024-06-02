from PIL import Image, ImageDraw, ImageFont
import mysql.connector

def image():
    img = Image.new('RGB', (400, 500), color="black")
    
    # Establishing connection to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Redranger@123",
        database="Kishore"
    )
    cursor = conn.cursor()
    
    try:
      cursor.execute("SELECT * FROM menu")
      data = cursor.fetchall()
      mdata = ""
      ndata = ""  # Initialize ndata here
      for d in data:
          for i in range(4, 20):
              if len(d[0]) == i:
                  s = 20 - i
                  extra = " " * s * 2
          mdata = mdata + str("     " + str(d[1]) + "      ") + "\n"
          ndata = ndata + str("     " + str(d[0]) + "      ") + "\n"  # Update ndata here
          print("Got menu image")
    except mysql.connector.DatabaseError as e:
        print("issue", e)
    finally:
        cursor.close()
        conn.close()



    f1 = ImageFont.truetype("arial.ttf", 19)
    f2 = ImageFont.truetype("arial.ttf", 17)
    f3 = ImageFont.truetype("arial.ttf", 13)
    f4 = ImageFont.truetype("arial.ttf", 14)
    d = ImageDraw.Draw(img)

    d.text((20, 10), "*" * 50, font=f1)
    d.text((20, 20), "PYTHON DEVELOPERS RESTAURANT", font=f1, fill=(95, 255, 247))
    d.text((20, 40), "*" * 50, font=f1)
    d.text((30, 60), "---------------------MENU--------------------", font=f2)
    d.text((60, 90), "DISH NAME", font=f3)
    d.text((270, 90), "RATE", font=f3)
    d.text((50, 110), ndata, fill=(255, 255, 0), font=f4)
    d.text((250, 110), mdata, fill=(255, 255, 0), font=f4)

    for i in range(5, 470, 8):
        d.text((5, i), "|", font=f1, fill=(255, 255, 0))
        d.text((390, i), "|", font=f1, fill=(255, 255, 0))
    
    for i in range(5, 390, 4):
        d.text((i, 480), "-", font=f1, fill=(255, 255, 0))
        d.text((i, -4), "-", font=f1, fill=(255, 255, 0))
    
    img.save('menu.jpg')
