trains = {
    "12301": {"name": "Rajdhani Express", "source": "Delhi", "dest": "Mumbai", "seats": 50, "fare": 2000},
    "12626": {"name": "Kerala Express", "source": "Delhi", "dest": "Kerala", "seats": 30, "fare": 1800},
    "12002": {"name": "Shatabdi Express", "source": "Delhi", "dest": "Bhopal", "seats": 20, "fare": 1200}}

bookings = []  
ticket_counter = 1001  

while True:
    print("\n====================================")
    print("    RAILWAY RESERVATION SYSTEM      ")
    print("====================================")
    print("1. View Available Trains")
    print("2. Book a Ticket")
    print("3. Cancel a Ticket")
    print("4. Check Ticket Status")
    print("5. Exit")
    print("====================================")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n--- AVAILABLE TRAINS ---")
        print("Train No | Train Name          | From       | To         | Seats | Fare")
        print("-" * 75)
        for train_no in trains:
            t = trains[train_no]
            print(f"{train_no}    | {t['name']:<19} | {t['source']:<10} | {t['dest']:<10} | {t['seats']:<5} | Rs.{t['fare']}")
        print("-" * 75)
        

    elif choice == "2":
        print("\n--- BOOK A TICKET ---")
        train_no = input("Enter the Train Number: ")
        
        
        if train_no in trains:
            selected_train = trains[train_no]
            
            
            if selected_train["seats"] > 0:
                passenger_name = input("Enter Passenger Name: ")
                passenger_age = input("Enter Passenger Age: ")
                
                selected_train["seats"] = selected_train["seats"] - 1
                
                
                ticket_id = str(ticket_counter)
                new_booking = {
                    "ticket_id": ticket_id,
                    "name": passenger_name,
                    "age": passenger_age,
                    "train_no": train_no,
                    "train_name": selected_train["name"],
                    "fare": selected_train["fare"]
                }
                bookings.append(new_booking)
                
                print("\n Ticket Booked Successfully!")
                print(f" Your Ticket ID is: {ticket_id}")
                ticket_counter = ticket_counter + 1
            else:
                print(" Sorry, no seats available on this train.")
        else:
            print(" Invalid Train Number!")

    
    elif choice == "3":
        print("\n--- CANCEL A TICKET ---")
        t_id = input("Enter your Ticket ID to cancel: ")
        
        found = False

        for ticket in bookings:
            if ticket["ticket_id"] == t_id:
                
                t_no = ticket["train_no"]
                trains[t_no]["seats"] = trains[t_no]["seats"] + 1
                
                
                bookings.remove(ticket)
                print(f" Ticket ID {t_id} has been cancelled successfully.")
                found = True
                break  
                
        if found == False:
            print(" Ticket ID not found.")

    elif choice == "4":
        print("\n--- CHECK TICKET STATUS ---")
        t_id = input("Enter your Ticket ID: ")
        
        found = False
        for ticket in bookings:
            if ticket["ticket_id"] == t_id:
                print("\n--- TICKET DETAILS ---")
                print(f"Ticket ID:      {ticket['ticket_id']}")
                print(f"Passenger Name: {ticket['name']}")
                print(f"Age:            {ticket['age']}")
                print(f"Train Name:     {ticket['train_name']} ({ticket['train_no']})")
                print(f"Fare:           Rs.{ticket['fare']}")
                print(f"Status:         Confirmed")
                print("----------------------")
                found = True
                break
                
        if found == False:
            print(" Ticket ID not found.")

    
    elif choice == "5":
        print("\nThank you for using the system. Goodbye!")
        break
        
    
    else:
        print(" Invalid choice! Please select a number from 1 to 5.")