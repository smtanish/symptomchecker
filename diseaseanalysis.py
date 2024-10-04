def display_precautions(disease_code):
    if disease_code == '1':
        print("Drug Reaction Precautions:\n- stop irritation\n- consult nearest hospital\n- stop taking drug\n- follow up")
    elif disease_code == '2':
        print("Malaria Precautions:\n- Consult nearest hospital\n- avoid oily food\n- avoid non veg food\n- keep mosquitos out")
    elif disease_code == '3':
        print("Allergy Precautions:\n- apply calamine\n- cover area with bandage\n- use ice to compress itching")
    elif disease_code == '4':
        print("Hypothyroidism Precautions:\n- reduce stress\n- exercise\n- eat healthy\n- get proper sleep")
    elif disease_code == '5':
        print("Psoriasis Precautions:\n- wash hands with warm soapy water\n- stop bleeding using pressure\n- consult doctor\n- salt baths")
    elif disease_code == '6':
        print("GERD Precautions:\n- avoid fatty spicy food\n- avoid lying down after eating\n- maintain healthy weight\n- exercise")
    elif disease_code == '7':
        print("Chronic Cholestasis Precautions:\n- cold baths\n- anti itch medicine\n- consult doctor\n- eat healthy")
    elif disease_code == '8':
        print("Hepatitis A Precautions:\n- Consult nearest hospital\n- wash hands thoroughly\n- avoid fatty spicy food\n- medication")
    elif disease_code == '9':
        print("Osteoarthritis Precautions:\n- acetaminophen\n- consult nearest hospital\n- follow up\n- salt baths")
    elif disease_code == '10':
        print("(Vertigo) Paroymsal Positional Vertigo Precautions:\n- lie down\n- avoid sudden changes in body position\n- avoid abrupt head movements\n- relax")
    elif disease_code == '11':
        print("Hypoglycemia Precautions:\n- lie down on side\n- check pulse\n- drink sugary drinks\n- consult doctor")
    elif disease_code == '12':
        print("Acne Precautions:\n- bathe twice daily\n- avoid fatty spicy food\n- drink plenty of water\n- avoid too many products")
    elif disease_code == '13':
        print("Diabetes Precautions:\n- have balanced diet\n- exercise\n- consult doctor\n- follow up")
    elif disease_code == '14':
        print("Impetigo Precautions:\n- soak affected area in warm water\n- use antibiotics\n- remove scabs with wet compressed cloth\n- consult doctor")
    elif disease_code == '15':
        print("Hypertension Precautions:\n- meditation\n- salt baths\n- reduce stress\n- get proper sleep")
    elif disease_code == '16':
        print("Peptic Ulcer Disease Precautions:\n- avoid fatty spicy food\n- consume probiotic food\n- eliminate milk\n- limit alcohol")
    elif disease_code == '17':
        print("Dimorphic Hemorrhoids (Piles) Precautions:\n- avoid fatty spicy food\n- consume witch hazel\n- warm bath with epsom salt\n- consume aloe vera juice")
    elif disease_code == '18':
        print("Common Cold Precautions:\n- drink vitamin C rich drinks\n- take vapour\n- avoid cold food\n- keep fever in check")
    elif disease_code == '19':
        print("Chicken Pox Precautions:\n- use neem in bathing\n- consume neem leaves\n- take vaccine\n- avoid public places")
    elif disease_code == '20':
        print("Cervical Spondylosis Precautions:\n- use heating pad or cold pack\n- exercise\n- take OTC pain reliever\n- consult doctor")
    elif disease_code == '21':
        print("Hyperthyroidism Precautions:\n- eat healthy\n- massage\n- use lemon balm\n- take radioactive iodine treatment")
    elif disease_code == '22':
        print("Urinary Tract Infection Precautions:\n- drink plenty of water\n- increase vitamin C intake\n- drink cranberry juice\n- take probiotics")
    elif disease_code == '23':
        print("Varicose Veins Precautions:\n- lie down flat and raise the leg high\n- use ointments\n- use vein compression\n- don’t stand still for long")
    elif disease_code == '24':
        print("AIDS Precautions:\n- avoid open cuts\n- wear PPE if possible\n- consult doctor\n- follow up")
    elif disease_code == '25':
        print("Paralysis (Brain Hemorrhage) Precautions:\n- massage\n- eat healthy\n- exercise\n- consult doctor")
    elif disease_code == '26':
        print("Typhoid Precautions:\n- eat high calorie vegetables\n- antibiotic therapy\n- consult doctor\n- medication")
    elif disease_code == '27':
        print("Hepatitis B Precautions:\n- consult nearest hospital\n- vaccination\n- eat healthy\n- medication")
    elif disease_code == '28':
        print("Fungal Infection Precautions:\n- bathe twice\n- use dettol or neem in bathing water\n- keep infected area dry\n- use clean clothes")
    elif disease_code == '29':
        print("Hepatitis C Precautions:\n- consult nearest hospital\n- vaccination\n- eat healthy\n- medication")
    elif disease_code == '30':
        print("Migraine Precautions:\n- meditation\n- reduce stress\n- use polaroid glasses in sun\n- consult doctor")
    elif disease_code == '31':
        print("Bronchial Asthma Precautions:\n- switch to loose clothing\n- take deep breaths\n- get away from trigger\n- seek help")
    elif disease_code == '32':
        print("Alcoholic Hepatitis Precautions:\n- stop alcohol consumption\n- consult doctor\n- medication\n- follow up")
    elif disease_code == '33':
        print("Jaundice Precautions:\n- drink plenty of water\n- consume milk thistle\n- eat fruits and high fibrous food\n- medication")
    elif disease_code == '34':
        print("Hepatitis E Precautions:\n- stop alcohol consumption\n- rest\n- consult doctor\n- medication")
    elif disease_code == '35':
        print("Dengue Precautions:\n- drink papaya leaf juice\n- avoid fatty spicy food\n- keep mosquitos away\n- keep hydrated")
    elif disease_code == '36':
        print("Hepatitis D Precautions:\n- consult doctor\n- medication\n- eat healthy\n- follow up")
    elif disease_code == '37':
        print("Heart Attack Precautions:\n- call ambulance\n- chew or swallow aspirin\n- keep calm")
    elif disease_code == '38':
        print("Pneumonia Precautions:\n- consult doctor\n- medication\n- rest\n- follow up")
    elif disease_code == '39':
        print("Arthritis Precautions:\n- exercise\n- use hot and cold therapy\n- try acupuncture\n- massage")
    elif disease_code == '40':
        print("Gastroenteritis Precautions:\n- stop eating solid food for a while\n- try taking small sips of water\n- rest\n- ease back into eating")
    elif disease_code == '41':
        print("Tuberculosis Precautions:\n- cover mouth\n- consult doctor\n- medication\n- rest")
    else:
        print("Invalid input. Please enter a valid number.")

def ask_another():
    response = input("Do you want to inquire about another disease? (yes/no): ").lower()
    if response == 'yes':
        return True
    elif response == 'no':
        print("Thank you for using the disease precaution checker!")
        return False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return ask_another()

while True:
    print("\nChoose a disease by entering the corresponding number:")
    print("1 = Drug Reaction")
    print("2 = Malaria")
    print("3 = Allergy")
    print("4 = Hypothyroidism")
    print("5 = Psoriasis")
    print("6 = GERD")
    print("7 = Chronic Cholestasis")
    print("8 = Hepatitis A")
    print("9 = Osteoarthritis")
    print("10 = (Vertigo) Paroymsal Positional Vertigo")
    print("11 = Hypoglycemia")
    print("12 = Acne")
    print("13 = Diabetes")
    print("14 = Impetigo")
    print("15 = Hypertension")
    print("16 = Peptic Ulcer Disease")
    print("17 = Dimorphic Hemorrhoids (Piles)")
    print("18 = Common Cold")
    print("19 = Chicken Pox")
    print("20 = Cervical Spondylosis")
    print("21 = Hyperthyroidism")
    print("22 = Urinary Tract Infection")
    print("23 = Varicose Veins")
    print("24 = AIDS")
    print("25 = Paralysis (Brain Hemorrhage)")
    print("26 = Typhoid")
    print("27 = Hepatitis B")
    print("28 = Fungal Infection")
    print("29 = Hepatitis C")
    print("30 = Migraine")
    print("31 = Bronchial Asthma")
    print("32 = Alcoholic Hepatitis")
    print("33 = Jaundice")
    print("34 = Hepatitis E")
    print("35 = Dengue")
    print("36 = Hepatitis D")
    print("37 = Heart Attack")
    print("38 = Pneumonia")
    print("39 = Arthritis")
    print("40 = Gastroenteritis")
    print("41 = Tuberculosis")

    user_input = input("Enter the number corresponding to the disease: ")

    display_precautions(user_input)

    if not ask_another():
        break


