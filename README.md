

**Bot ko Group aur Channel me Kaise Add Karein (Step-by-Step)**

* **Step 1: Public Group me Bot Add Karna**
  * Apne Public Group ki settings me jayein ya Bot ke `/start` message me diye gaye **"➕ Add Me To Your Group"** button par click karein.
  * Bot ko apne group me select karke add kar dein.
  * Bot ko group me **Administrator** bana dein taaki wo messages read kar sake aur replies bhej sake.

* **Step 2: Private Channel ko Link Karna**
  * Apne Private Channel me bot ko **Administrator** add karein (taaki bot channel ke contents read kar sake).
  * Apne Private Channel ki ID pata karein (e.g., `-100xxxxxxxxxx`). ID nikalne ke liye aap kisi forward bot ka use kar sakte hain ya channel ki post ko group me forward karke inspect kar sakte hain.
  * Apne Public Group me jayein aur ye command bhejein:
    `/setchannel -100xxxxxxxxxx` (yahan `-100xxxxxxxxxx` ki jagah apne private channel ki real ID daalein).
  * Bot success message dega ki channel link ho chuka hai. Ab koi bhi user group me file name ya year likhega toh bot us channel ke database se match karke turant reply karega!

