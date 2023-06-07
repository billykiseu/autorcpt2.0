#generate recipts
def generate_pdf(transaction):
    # Generate a unique receipt number
    with transaction.atomic():
        receipt = Receipt.objects.create()
        receipt_number = f"RECEIPT-{receipt.id:05}"
        receipt.receipt_number = receipt_number
        receipt.save()
        
    # Define the context for the template
    context = {
        'receipt_number': receipt_number,
        'house_number': transaction['HouseNumber'],
        'name': transaction['Name'],
        'date': transaction['Date'],
        'phone': transaction['Phone'],
        'description': transaction['Description'],
        'amount': transaction['Amount'],
        'email': transaction['Email'],
    }

    # Set the path and name for the output file
    date_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    phone=str(transaction['Phone'])
    if phone.startswith('254'):
        phone_number = '0' + phone[3:].zfill(9)
    else:
        phone_number = phone.zfill(10)[-10:]

    file_name = f"{phone_number}_{transaction['Name']}_{date_str}.pdf"
    pdf_path = os.path.join(settings.STATIC_ROOT, 'receipts', file_name)

    # Load the template
    template = get_template('receipt_template.html')

    # Render the template with the context
    html = template.render(context)

    # Modify the contents of the page
    soup = BeautifulSoup(html, 'html.parser')
    soup.find(id='house_number').string = str(transaction['HouseNumber'])
    soup.find(id='name').string = str(transaction['Name'])
    soup.find(id='date').string = str(transaction['Date'])
    soup.find(id='phone').string = str(phone_number)
    soup.find(id='description').string = str(transaction['Description'])
    soup.find(id='amount').string = str(transaction['Amount'])
    soup.find(id='email').string = str(transaction['Email'])
    html = str(soup)

    # Create a PDF file
    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    # Check if the PDF was successfully created
    if not pdf.err:
        # Save the PDF file
        with open(pdf_path, 'wb') as file:
            file.write(result.getvalue())
        # Return the PDF file as a BytesIO object
        result.seek(0)
        return result
    
    error_message = f"Error creating PDF: {pdf.err}"
    error_bytes = BytesIO(error_message.encode('utf-8'))
    return error_bytes
