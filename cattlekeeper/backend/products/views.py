from django.http import JsonResponse

def get_all_products(request):
    products = [
        {'id': 1, 'name': 'Alimento para ganado', 'price': 25.99, 'image': 'https://static.vecteezy.com/system/resources/thumbnails/049/045/108/small_2x/hay-bale-pixel-art-for-your-needs-vector.jpg'},
        {'id': 2, 'name': 'Suplementos vitamínicos', 'price': 15.50, 'image': 'https://static.vecteezy.com/system/resources/previews/023/873/447/non_2x/health-vitamin-bottle-game-pixel-art-illustration-vector.jpg'},
        {'id': 3, 'name': 'Vacuna contra aftosa', 'price': 12.00, 'image': 'https://as1.ftcdn.net/jpg/04/37/33/04/1000_F_437330478_DWqifW7UcrLLKIVrSEhWVlBex5JhvFJy.jpg'},
        {'id': 4, 'name': 'Bebedero automático', 'price': 45.75, 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTutoqkzuSo_EM2mkD6r9tZ5k7zo2JUu1W-jA&s'},
        {'id': 5, 'name': 'Esquila eléctrica', 'price': 80.00, 'image': 'https://img.freepik.com/psd-premium/pixel-art-sierra-mango-amarillo_901483-17.jpg'},
        {'id': 6, 'name': 'Sales minerales', 'price': 18.90, 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYDUFR3koMz-OYH8TK9mTWBWidsLf_RQNaMw&s'},
        {'id': 7, 'name': 'Medicamento antiparasitario', 'price': 22.50, 'image': 'https://www.shutterstock.com/image-vector/medicine-pill-bottle-container-child-260nw-2029148558.jpg'},
        {'id': 8, 'name': 'Cercado eléctrico', 'price': 120.00, 'image': 'https://static.vecteezy.com/system/resources/previews/022/284/738/non_2x/wooden-fence-in-pixel-art-style-vector.jpg'},
    ]
    return JsonResponse(products, safe=False)
