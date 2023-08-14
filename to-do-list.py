
list = []

# Kullanıcıdan alınan girdileri listeye eklemek
def add_task(list):
    task = input("Bugünkü görevi giriniz: ")
    list.append(task)
    print("Görev başarıyla listeye eklendi.")

# Listede bulunan görevleri göstermek
def show_tasks(list):
    print("Yapılacak Görevler: ")
    for task in list:
        print("- " + task)

# Listeden görevleri silmek
def delete_task(list):
    task = input("Silmek istediğiniz görevi girin: ")
    if task in list:
        list.remove(task)
        print("Görev başarıyla silindi.")
    else:
        print("Görev bulunamadı.")

while True:
    print("\nTo-Do List Uygulaması")
    print("1. Görev Ekle")
    print("2. Görevleri Göster")
    print("3. Görev Sil")
    print("4. Çıkış")
    choice = input("Seçiminiz (1/2/3/4): ")
    
    if choice == "1":
        add_task(list)
    elif choice == "2":
        show_tasks(list)
    elif choice == "3":
        delete_task(list)
    elif choice == "4":
        print("Uygulamadan çıkılıyor..")
        break
    else:
        print("Geçersiz seçim yapıldı. Lütfen tekrar deneyin.")