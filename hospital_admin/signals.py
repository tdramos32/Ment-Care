

# Update and delete signals
# @receiver(post_save, sender=Admin_Information)
# def updateUser(sender, instance, created, **kwargs):
#     # user.profile or below (1-1 relationship goes both ways)
#     admin = instance
#     user = admin.user

#     if created == False:
#         user.first_name = admin.name
#         user.username = admin.username
#         user.email = admin.email
#         user.save()


# @receiver(post_save, sender=Patient)
# def updateUser(sender, instance, created, **kwargs):
#     # user.profile or below (1-1 relationship goes both ways)
#     patient = instance
#     user = patient.user

#     if created == False:
#         user.first_name = patient.name
#         user.username = patient.username
#         user.email = patient.email
#         user.save()