def add_phone_and_address(user, mobile_num, address):
    UserPhone.objects.create(user, phone_number=mobile_num)
    if address:
        UserAddress.objects.create(**address)
    pass
