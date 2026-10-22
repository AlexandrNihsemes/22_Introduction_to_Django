from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    Контроллер главной страницы.
    Рендерит шаблон home.html
    """
    return render(request, 'home.html')

def contacts(request):
    """
    Контроллер страницы контактов.
    Рендерит шаблон contacts.html
    Обрабатывает форму обратной связи.
    """
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        
        # Здесь можно добавить логику сохранения данных
        # Например, создать модель ContactMessage и сохранить в БД
        
        # Возвращаем сообщение об успешной отправке
        return render(request, 'contacts.html', {
            'success': True,
            'name': name,
        })
    
    # GET-запрос — просто отображаем страницу
    return render(request, 'contacts.html')