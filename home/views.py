from django.shortcuts import render

posts = [
    {
        'author': 'Damian Wilusz',
        'title': 'Ogłoszenie nr. 1',
        'content': ' Sed eget rutrum augue. Maecenas sem odio, imperdiet quis augue a, pellentesque blandit ex. Suspendisse potenti. Phasellus sed elementum elit. Vestibulum non gravida ipsum. Sed tempus dui ex, id volutpat risus venenatis et. Sed luctus lobortis laoreet. Sed vestibulum in lorem at eleifend. Vestibulum et turpis quis augue tristique sagittis. Ut pulvinar sed nisi non ornare. Vestibulum aliquam, dui sed tempor egestas, nunc tellus aliquet metus, in dapibus sem tortor quis sapien. Aenean quam quam, eleifend a ultrices vitae, hendrerit ac massa. Aliquam in arcu vel diam placerat bibendum. Integer faucibus, nulla vitae blandit consequat, ex nulla varius ex, non malesuada turpis orci eget nisl. Proin lorem ligula, imperdiet quis diam et, interdum imperdiet ex. Nullam dictum convallis sem, a tincidunt lacus maximus pretium. ',
        'date_posted': 'June 26, 2022',
        'category': 'Ubrania',
        'city': 'Rzeszów'
    },
    {
        'author': 'Diana Blazejowska',
        'title': 'Ogłoszenie nr. 2',
        'content': ' Sed eget rutrum augue. Maecenas sem odio, imperdiet quis augue a, pellentesque blandit ex. Suspendisse potenti. Phasellus sed elementum elit. Vestibulum non gravida ipsum. Sed tempus dui ex, id volutpat risus venenatis et. Sed luctus lobortis laoreet. Sed vestibulum in lorem at eleifend. Vestibulum et turpis quis augue tristique sagittis. Ut pulvinar sed nisi non ornare. Vestibulum aliquam, dui sed tempor egestas, nunc tellus aliquet metus, in dapibus sem tortor quis sapien. Aenean quam quam, eleifend a ultrices vitae, hendrerit ac massa. Aliquam in arcu vel diam placerat bibendum. Integer faucibus, nulla vitae blandit consequat, ex nulla varius ex, non malesuada turpis orci eget nisl. Proin lorem ligula, imperdiet quis diam et, interdum imperdiet ex. Nullam dictum convallis sem, a tincidunt lacus maximus pretium. ',
        'date_posted': 'June 27, 2022',
        'category': 'Samochod',
        'city': 'Rzeszów'
    },
    {
        'author': 'Diana Blazejowska',
        'title': 'Ogłoszenie nr. 3',
        'content': ' Sed eget rutrum augue. Maecenas sem odio, imperdiet quis augue a, pellentesque blandit ex. Suspendisse potenti. Phasellus sed elementum elit. Vestibulum non gravida ipsum. Sed tempus dui ex, id volutpat risus venenatis et. Sed luctus lobortis laoreet. Sed vestibulum in lorem at eleifend. Vestibulum et turpis quis augue tristique sagittis. Ut pulvinar sed nisi non ornare. Vestibulum aliquam, dui sed tempor egestas, nunc tellus aliquet metus, in dapibus sem tortor quis sapien. Aenean quam quam, eleifend a ultrices vitae, hendrerit ac massa. Aliquam in arcu vel diam placerat bibendum. Integer faucibus, nulla vitae blandit consequat, ex nulla varius ex, non malesuada turpis orci eget nisl. Proin lorem ligula, imperdiet quis diam et, interdum imperdiet ex. Nullam dictum convallis sem, a tincidunt lacus maximus pretium. ',
        'date_posted': 'June 27, 2022',
        'category': 'Samochod',
        'city': 'Rzeszów'
    },
    {
        'author': 'Diana Blazejowska',
        'title': 'Ogloszenie nr. 4',
        'content': ' Sed eget rutrum augue. Maecenas sem odio, imperdiet quis augue a, pellentesque blandit ex. Suspendisse potenti. Phasellus sed elementum elit. Vestibulum non gravida ipsum. Sed tempus dui ex, id volutpat risus venenatis et. Sed luctus lobortis laoreet. Sed vestibulum in lorem at eleifend. Vestibulum et turpis quis augue tristique sagittis. Ut pulvinar sed nisi non ornare. Vestibulum aliquam, dui sed tempor egestas, nunc tellus aliquet metus, in dapibus sem tortor quis sapien. Aenean quam quam, eleifend a ultrices vitae, hendrerit ac massa. Aliquam in arcu vel diam placerat bibendum. Integer faucibus, nulla vitae blandit consequat, ex nulla varius ex, non malesuada turpis orci eget nisl. Proin lorem ligula, imperdiet quis diam et, interdum imperdiet ex. Nullam dictum convallis sem, a tincidunt lacus maximus pretium. ',
        'date_posted': 'June 27, 2022',
        'category': 'Samochod',
        'city': 'Rzeszów'
    },
    {
        'author': 'Diana Blazejowska',
        'title': 'Ogloszenie nr. 5',
        'content': ' Sed eget rutrum augue. Maecenas sem odio, imperdiet quis augue a, pellentesque blandit ex. Suspendisse potenti. Phasellus sed elementum elit. Vestibulum non gravida ipsum. Sed tempus dui ex, id volutpat risus venenatis et. Sed luctus lobortis laoreet. Sed vestibulum in lorem at eleifend. Vestibulum et turpis quis augue tristique sagittis. Ut pulvinar sed nisi non ornare. Vestibulum aliquam, dui sed tempor egestas, nunc tellus aliquet metus, in dapibus sem tortor quis sapien. Aenean quam quam, eleifend a ultrices vitae, hendrerit ac massa. Aliquam in arcu vel diam placerat bibendum. Integer faucibus, nulla vitae blandit consequat, ex nulla varius ex, non malesuada turpis orci eget nisl. Proin lorem ligula, imperdiet quis diam et, interdum imperdiet ex. Nullam dictum convallis sem, a tincidunt lacus maximus pretium. ',
        'date_posted': 'June 27, 2022',
        'category': 'Samochod',
        'city': 'Rzeszów'
    },
    {
        'author': 'Diana Blazejowska',
        'title': 'Ogloszenie nr. 6',
        'content': ' Sed eget rutrum augue. Maecenas sem odio, imperdiet quis augue a, pellentesque blandit ex. Suspendisse potenti. Phasellus sed elementum elit. Vestibulum non gravida ipsum. Sed tempus dui ex, id volutpat risus venenatis et. Sed luctus lobortis laoreet. Sed vestibulum in lorem at eleifend. Vestibulum et turpis quis augue tristique sagittis. Ut pulvinar sed nisi non ornare. Vestibulum aliquam, dui sed tempor egestas, nunc tellus aliquet metus, in dapibus sem tortor quis sapien. Aenean quam quam, eleifend a ultrices vitae, hendrerit ac massa. Aliquam in arcu vel diam placerat bibendum. Integer faucibus, nulla vitae blandit consequat, ex nulla varius ex, non malesuada turpis orci eget nisl. Proin lorem ligula, imperdiet quis diam et, interdum imperdiet ex. Nullam dictum convallis sem, a tincidunt lacus maximus pretium. ',
        'date_posted': 'June 27, 2022',
        'category': 'Samochod',
        'city': 'Rzeszów'
    }, 
    {
        'author': 'Diana Blazejowska',
        'title': 'Ogloszenie nr. 7',
        'content': ' Sed eget rutrum augue. Maecenas sem odio, imperdiet quis augue a, pellentesque blandit ex. Suspendisse potenti. Phasellus sed elementum elit. Vestibulum non gravida ipsum. Sed tempus dui ex, id volutpat risus venenatis et. Sed luctus lobortis laoreet. Sed vestibulum in lorem at eleifend. Vestibulum et turpis quis augue tristique sagittis. Ut pulvinar sed nisi non ornare. Vestibulum aliquam, dui sed tempor egestas, nunc tellus aliquet metus, in dapibus sem tortor quis sapien. Aenean quam quam, eleifend a ultrices vitae, hendrerit ac massa. Aliquam in arcu vel diam placerat bibendum. Integer faucibus, nulla vitae blandit consequat, ex nulla varius ex, non malesuada turpis orci eget nisl. Proin lorem ligula, imperdiet quis diam et, interdum imperdiet ex. Nullam dictum convallis sem, a tincidunt lacus maximus pretium. ',
        'date_posted': 'June 27, 2022',
        'category': 'Samochod',
        'city': 'Rzeszów'
    },
    {
        'author': 'Diana Blazejowska',
        'title': 'Ogloszenie nr. 8',
        'content': ' Sed eget rutrum augue. Maecenas sem odio, imperdiet quis augue a, pellentesque blandit ex. Suspendisse potenti. Phasellus sed elementum elit. Vestibulum non gravida ipsum. Sed tempus dui ex, id volutpat risus venenatis et. Sed luctus lobortis laoreet. Sed vestibulum in lorem at eleifend. Vestibulum et turpis quis augue tristique sagittis. Ut pulvinar sed nisi non ornare. Vestibulum aliquam, dui sed tempor egestas, nunc tellus aliquet metus, in dapibus sem tortor quis sapien. Aenean quam quam, eleifend a ultrices vitae, hendrerit ac massa. Aliquam in arcu vel diam placerat bibendum. Integer faucibus, nulla vitae blandit consequat, ex nulla varius ex, non malesuada turpis orci eget nisl. Proin lorem ligula, imperdiet quis diam et, interdum imperdiet ex. Nullam dictum convallis sem, a tincidunt lacus maximus pretium. ',
        'date_posted': 'June 27, 2022',
        'category': 'Samochod',
        'city': 'Rzeszów'
    },    
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home/homepage.html', context)
