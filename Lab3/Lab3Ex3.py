import re
import os.path

def read_file_path():
    while True:
        file_path = input("Introduceți calea către fișierul text: ")
        if os.path.exists(file_path):
            return file_path
        else:
            print("Calea specificată nu există. Vă rugăm să introduceți o cale validă.")

def verify_invoice_format(file_path):
    with open(file_path, 'r') as file:
        invoice_content = file.read()

    # Define regular expressions for each section of the invoice
    # bill_meta_regex = r"Emission Date: [0-3][0-9]-[0-1][0-2]-[20][0-2][0-6]"
    client_info_regex = r"Client: (.+)"
    product_details_regex = r"Produs: (.+), Pret: (\d+\.\d+) (lei), TVA: (\d+\.\d+) (lei), Cantitate: (\d+)"
    
    # Match regular expressions against the invoice content
    bill_meta_match = re.search(bill_meta_regex, invoice_content)
    client_match = re.search(client_info_regex, invoice_content)
    product_matches = re.findall(product_details_regex, invoice_content)

    # Check if all sections are present
    errors = []
    # if not bill_meta_match:
    #    errors.append("Datele de emitere ale facturii sunt eronate.")
    if not client_match:
        errors.append("Datele clientului sunt eronate.")

    # Display errors, if any
    if errors:
        print("Erori în formatul facturii:")
        for error in errors:
            print("-", error)
    else:
        print("Factura respectă formatul specificat.")

if __name__ == "__main__":
    file_path = read_file_path()
    verify_invoice_format(file_path)