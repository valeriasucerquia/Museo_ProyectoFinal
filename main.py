from controller.controllerObradeArte import ArtController

controller = ArtController()
# controller.add_escultura(
#     nombre="La Gioconda2",
#     autor="Leonardo da Vinci",
#     en_venta=False,
#     volumen="77 x 53 cm",
#     material="Óleo sobre tabla"
# )

# controller.add_pintura(
#     nombre="La Gioconda",
#     autor="bedoya",
#     en_venta= True,
#     dimensiones="77 x 53 cm",
#     tecnica="Témpera",
#     retrato = True
# )

# controller.add_pintura(
#     nombre="IPHONE CRISTAL",
#     autor="bedoya",
#     en_venta= False,
#     dimensiones="77 x 53 cm",
#     tecnica="Acrílico",
#     retrato = False
# )

#print(type(controller.get_artwork_by_name("La Gioconda255")))
#print(controller.get_artwork_by_type("Escultura"))
#print(controller.get_artwork_by_type("Pintura"))
#r = controller.delete_artwork_by_name("La Gioconda2")
a = controller.all_view_artwork()
print(a)