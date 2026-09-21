import smtplib

my_email = "d######t@gmail.com"
## Generate the app password in google > security
passoword = "### # ## # # #"

with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()
    connection.login(user=my_email, password=passoword)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="####@gmail.com", 
        msg="Subject:Hello\n\nThis is the body of my email")

    connection.close()


