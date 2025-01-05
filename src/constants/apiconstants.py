
class APIConstants:
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def create_booking_url(self):
        return "https://restful-booker.herokuapp.com/booking/"

    def create_auth_url(self):
        return "https://restful-booker.herokuapp.com/auth"

    def patch_put_del_url(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)