import sqlite3
import pandas as pd

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('chinook.db')

# Invoice va Customer jadvallarini o'qib olish
df_invoice = pd.read_sql("SELECT CustomerId, Total FROM Invoices", conn)
df_customer = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customers", conn)

# Har bir mijoz bo‘yicha jami xarajatni hisoblash
df_total = df_invoice.groupby("CustomerId")["Total"].sum().reset_index()

# Mijoz ismlari bilan birlashtirish
df_total = df_total.merge(df_customer, on="CustomerId")

# Yangi ustun: To‘liq ism
df_total["FullName"] = df_total["FirstName"] + " " + df_total["LastName"]

# Ustunlarni tartibga solish
df_total = df_total[["CustomerId", "FullName", "Total"]]

# Natijani ko‘rsatish
print(df_total.head())



#2

df_invoice = pd.read_sql("SELECT CustomerId, Total FROM Invoices", connection)
df_customer = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customers", connection)


df_total = df_invoices.groupby("CustomerId")["Total"].sum().reset_index()

df_total = df_total.merge(df_customer, on="CustomerId")

df_total["FullName"] = df_total["FirstName"] + " " + df_total["LastName"]

# Yuqoridan pastga saralash va eng yuqori 5 ta mijozni olish
top5 = df_total.sort_values(by="Total", ascending=False).head(5)

# Natijani tanlab ko‘rsatish
print(top5[["CustomerId", "FullName", "Total"]])


#3

import sqlite3
import pandas as pd

# Baza bilan bog'lanish
conn = sqlite3.connect('chinook.db')

# Jadval ma'lumotlarini olish
df_invoice = pd.read_sql("SELECT CustomerId, Total FROM Invoices", conn)
df_customer = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customers", conn)

# Har bir mijoz bo'yicha jami sarflangan summa
df_total = df_invoice.groupby("CustomerId")["Total"].sum().reset_index()

# Mijoz ma'lumotlarini qo‘shish
df_total = df_total.merge(df_customer, on="CustomerId")

# To‘liq ism ustunini yaratish
df_total["FullName"] = df_total["FirstName"] + " " + df_total["LastName"]

# Saralash va faqat top 5 ni olish
top5 = df_total.sort_values(by="Total", ascending=False).head(5)

# Tanlangan ustunlarni ko‘rsatish
print(top5[["CustomerId", "FullName", "Total"]])



import sqlite3
import pandas as pd

# Bazaga ulanish
conn = sqlite3.connect('chinook.db')

# Jadval ma'lumotlarini olish
invoice_df = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoices", conn)
invoiceline_df = pd.read_sql("SELECT InvoiceId, TrackId FROM Invoice_items", conn)
track_df = pd.read_sql("SELECT TrackId, AlbumId FROM Tracks", conn)
customer_df = pd.read_sql("SELECT CustomerId FROM Customers", conn)

# Har bir albomda nechta trek borligini aniqlash
album_track_counts = track_df.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracksInAlbum"}, inplace=True)

# InvoiceLine + Track = qaysi InvoiceId da qaysi albomdan trek sotib olingan
invoice_tracks = invoiceline_df.merge(track_df, on="TrackId")

# Har bir invoice va album uchun nechta trek sotib olingan?
invoice_album_track_counts = (
    invoice_tracks.groupby(["InvoiceId", "AlbumId"])["TrackId"]
    .count()
    .reset_index()
    .rename(columns={"TrackId": "TracksPurchased"})
)

# Albomdagi umumiy trek sonini qo‘shish
invoice_album_full = invoice_album_track_counts.merge(album_track_counts, on="AlbumId")

# Full album sotib olinganmi? (agar barcha treklar sotib olingan bo‘lsa)
invoice_album_full["IsFullAlbum"] = invoice_album_full["TracksPurchased"] == invoice_album_full["TotalTracksInAlbum"]

# Har bir invoice bo‘yicha — hech bo‘lmasa 1 ta full album olganlar
invoice_full_album = invoice_album_full.groupby("InvoiceId")["IsFullAlbum"].any().reset_index()

# InvoiceId -> CustomerId bilan birlashtirish
invoice_full_album = invoice_full_album.merge(invoice_df, on="InvoiceId")

# Endi, har bir Customer uchun: u biron marta full album olganmi?
customer_album_pref = invoice_full_album.groupby("CustomerId")["IsFullAlbum"].any().reset_index()
# Faqat individual treklar olganlar: IsFullAlbum == False
individual_only_customers = customer_album_pref[customer_album_pref["IsFullAlbum"] == False]

# Umumiy mijozlar soni
total_customers = customer_df["CustomerId"].nunique()

# Individual buyers soni
individual_only_count = individual_only_customers["CustomerId"].nunique()

# Foiz hisoblash
percentage = (individual_only_count / total_customers) * 100

# Natijani chiqarish
print(f"{individual_only_count} of {total_customers} customers ({percentage:.2f}%) bought only individual tracks.")



import sqlite3
import pandas as pd

# Bazaga ulanish
conn = sqlite3.connect('chinook.db')

# Jadval ma'lumotlarini olish
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoices", conn)
invoice_lines = pd.read_sql("SELECT InvoiceId, TrackId FROM Invoice_items", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM Tracks", conn)
customers = pd.read_sql("SELECT CustomerId FROM Customers", conn)

# 1. Har bir albomda nechta trek bor?
album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "AlbumTotalTracks"}, inplace=True)

# 2. InvoiceLine + Track = qaysi InvoiceId da qaysi albomdan nechta trek olingan
invoice_track_album = invoice_lines.merge(tracks, on="TrackId")

# 3. Har bir InvoiceId + AlbumId bo‘yicha nechta trek olinganini topamiz
invoice_album_track_counts = (
    invoice_track_album.groupby(["InvoiceId", "AlbumId"])["TrackId"]
    .count()
    .reset_index()
    .rename(columns={"TrackId": "TracksPurchased"})
)

# 4. Albomdagi jami treklar bilan birlashtiramiz
invoice_album_full = invoice_album_track_counts.merge(album_track_counts, on="AlbumId")

# 5. Har bir invoice bo‘yicha: to‘liq albom olinganmi?
invoice_album_full["IsFullAlbum"] = invoice_album_full["TracksPurchased"] == invoice_album_full["AlbumTotalTracks"]

# 6. Har bir invoice uchun hech bo‘lmasa 1 ta full album olinganmi?
invoice_full_album = invoice_album_full.groupby("InvoiceId")["IsFullAlbum"].any().reset_index()

# 7. InvoiceId orqali CustomerId ni qo‘shamiz
invoice_customer_album = invoice_full_album.merge(invoices, on="InvoiceId")

# 8. Har bir CustomerId bo‘yicha: u hech qachon full album olmagan bo‘lsa => individual buyer
customer_album_pref = invoice_customer_album.groupby("CustomerId")["IsFullAlbum"].any().reset_index()
customer_album_pref["PrefersIndividualTracks"] = customer_album_pref["IsFullAlbum"] == False

# 9. Faqat individual tracks olgan mijozlar soni
individual_pref_count = customer_album_pref["PrefersIndividualTracks"].sum()

# 10. Umumiy mijozlar soni
total_customers = customers["CustomerId"].nunique()

# 11. Foiz hisoblash
percentage = (individual_pref_count / total_customers) * 100

# 12. Natijani chiqaramiz
print(f"{individual_pref_count} of {total_customers} customers ({percentage:.2f}%) prefer individual tracks.")



import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('chinook.db')

# Load necessary tables
invoice_lines = pd.read_sql("SELECT InvoiceId, TrackId FROM Invoice_items", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoices", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM Tracks", conn)
customers = pd.read_sql("SELECT CustomerId FROM Customers", conn)

# Number of tracks per album
album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "AlbumTotalTracks"}, inplace=True)

# Merge invoice lines with track info to get album info per invoice
invoice_track_album = invoice_lines.merge(tracks, on="TrackId")

# Count how many tracks from each album were purchased per invoice
invoice_album_counts = invoice_track_album.groupby(["InvoiceId", "AlbumId"])["TrackId"].count().reset_index()
invoice_album_counts.rename(columns={"TrackId": "TracksPurchased"}, inplace=True)
# Merge to get total album tracks
invoice_album_info = invoice_album_counts.merge(album_track_counts, on="AlbumId")
invoice_album_info["IsFullAlbum"] = invoice_album_info["TracksPurchased"] == invoice_album_info["AlbumTotalTracks"]

# Add customer info
invoice_customer = invoices[["InvoiceId", "CustomerId"]]
invoice_album_info = invoice_album_info.merge(invoice_customer, on="InvoiceId")

# For each customer, check if they ever purchased a full album
customer_album_summary = invoice_album_info.groupby("CustomerId")["IsFullAlbum"].any().reset_index()

# Classify customer type
customer_album_summary["Category"] = customer_album_summary["IsFullAlbum"].apply(
    lambda x: "Full Album Buyer" if x else "Individual Track Buyer"
)

# Count customers per category
summary = customer_album_summary["Category"].value_counts(normalize=True).reset_index()
summary.columns = ["Category", "Percentage"]
summary["Percentage"] *= 100

# Show summary
print(summary)
