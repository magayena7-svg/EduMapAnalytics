import mysql.connector
import matplotlib.pyplot as plt

# Koneksi ke MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # isi sesuai password MySQL kamu
    database="edumap"
)
cursor = conn.cursor()

# Ambil data jumlah lulus/tidak lulus
cursor.execute("""
    SELECT 
      SUM(CASE WHEN score >= 70 THEN 1 ELSE 0 END) AS lulus,
      SUM(CASE WHEN score < 70 THEN 1 ELSE 0 END) AS tidak_lulus
    FROM students;
""")
result = cursor.fetchone()
lulus, tidak_lulus = result

# Buat pie chart
labels = ['Lulus', 'Tidak Lulus']
values = [lulus, tidak_lulus]
colors = ['green', 'red']

plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Persentase Mahasiswa Lulus vs Tidak Lulus')
plt.show()

conn.close()