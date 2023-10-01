from django.shortcuts import render, redirect
from .models import hobbies, games

def home(request):
    hobbies_list = hobbies.objects.all()  # Recupere a lista de hobbies
    game_list = games.objects.all()
    return render(request, "home.html", context={"hobbies": hobbies_list, "acao": game_list})


def create_game(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        genero = request.POST.get("genero")
        competicao = request.POST.get("competicao")
        esforcoComputacional = request.POST.get("esforcoComputacional")
        frequencia = request.POST.get("frequencia")
        
        # Create a new game object here using the retrieved data and save it.
        new_game = games(
            titulo=titulo,
            genero=genero,
            competicao=competicao,
            esforcoComputacional=esforcoComputacional,
            frequencia=frequencia
        )
        new_game.save()
        
        return redirect("home")
    
    return render(request, "forms.html", context={"acao": "Adicionar"})

def update_game(request, id):
    game = games.objects.get(id=id)
    if request.method == "POST":
        game.titulo = request.POST.get("titulo")
        game.genero = request.POST.get("genero")
        game.competicao = request.POST.get("competicao")
        game.esforcoComputacional = request.POST.get("esforcoComputacional")
        game.frequencia = request.POST.get("frequencia")
        game.save()
        return redirect("home")
    
    return render(request, "forms.html", context={"game": game})

def delete_game(request, id):
    game = games.objects.get(id=id)
    if request.method == "POST" and "confirma" in request.POST:
        game.delete()
        return redirect("home")
    
    return render(request, "areyousure.html", context={"game": game})

from django.shortcuts import render, redirect
from .models import hobbies, games


def create_hobby(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        genero = request.POST.get("genero")
        competicao = request.POST.get("competicao")
        tipo = request.POST.get("tipo")
        amigos = request.POST.get("amigos")
        
        # Crie um novo objeto de hobby aqui usando os dados recuperados e salve-o.
        novo_hobby = hobbies(
            titulo=titulo,
            genero=genero,
            competicao=competicao,
            tipo=tipo,
            amigos=amigos
        )
        novo_hobby.save()
        
        return redirect("home")
    
    return render(request, "forms.html", context={"acao": "Adicionar Hobbie"})



# ... outras views ...

def update_hobby(request, id):
    hobby = hobbies.objects.get(id=id)
    if request.method == "POST":
        # Recupere os dados atualizados do formulário
        titulo = request.POST.get("titulo")
        genero = request.POST.get("genero")
        competicao = request.POST.get("competicao")
        tipo = request.POST.get("tipo")
        amigos = request.POST.get("amigos")
        
        # Atualize os campos do hobby com os novos dados
        hobby.titulo = titulo
        hobby.genero = genero
        hobby.competicao = competicao
        hobby.tipo = tipo
        hobby.amigos = amigos
        
        # Salve as atualizações no banco de dados
        hobby.save()
        
        return redirect("home")
    
    return render(request, "forms.html", context={"acao": "Atualizar Hobbie", "hobby": hobby})


def delete_hobby(request, id):
    hobby = hobbies.objects.get(id=id)
    if request.method == "POST" and "confirma" in request.POST:
        hobby.delete()
        return redirect("home")
    
    return render(request, "areyousure.html", context={"hobby": hobby})
