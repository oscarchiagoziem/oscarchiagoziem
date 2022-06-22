from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import  HttpResponseRedirect
from .models import Sheet, Audio, Video, Document
from account.models import Campus, Executive_Akpugo
from about.models import About
from django.contrib import messages
import fitz, os, shutil


# Create your views here.

def index(request):
    try:
        about = About.objects.get(title='About Madonna Central Choir')
    except Exception:
        about = ''
    context = {'about': about}
    return render(request, 'index.html', context)


def library(request):
    audio = Audio.objects.filter()
    audio_count = audio.count
    sheet = Sheet.objects.filter()
    sheet_count = sheet.count
    video = Video.objects.filter()
    video_count = video.count
    document = Document.objects.filter()
    document_count = document.count

    try:
        about = About.objects.get(title='About Madonna Central Choir')
    except Exception:
        about = ''
    context = {'sheet_count': sheet_count,
               'audio_count': audio_count,
               'video_count': video_count,
               'document_count': document_count,
               'about': about}
    return render(request, 'library/library.html', context)


def sheet(request):
    if 'q' in request.GET:
        q = request.GET['q']
        sheet = Sheet.objects.filter(title__icontains=q, ) | \
                Sheet.objects.filter(composer__icontains=q, ) | \
                Sheet.objects.filter(type__icontains=q, ) | \
                Sheet.objects.filter(part_of_calender__icontains=q, ) | \
                Sheet.objects.filter(part_of_mass__icontains=q, )

        paginator = Paginator(sheet, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        search = 1

        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'sheet': sheet,
                   'page_obj': page_obj,
                   'search': search,
                   'about': about}
        return render(request, 'library/sheet.html', context)
    else:
        sheet = Sheet.objects.filter()
        liturgy_sheet = Sheet.objects.filter(type='Liturgy')
        liturgy_sheet_count = liturgy_sheet.count
        classical_sheet = Sheet.objects.filter(type='Classical')
        classical_sheet_count = classical_sheet.count
        cultural_sheet = Sheet.objects.filter(type='Cultural')
        cultural_sheet_count = cultural_sheet.count
        others_sheet = Sheet.objects.filter(type='Others')
        others_sheet_count = others_sheet.count
        search = 0
        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'sheet': sheet,
                   'liturgy_sheet_count': liturgy_sheet_count,
                   'classical_sheet_count': classical_sheet_count,
                   'cultural_sheet_count': cultural_sheet_count,
                   'others_sheet_count': others_sheet_count,
                   'search': search,
                   'about': about,
                   }
        return render(request, 'library/sheet.html', context)


def sheet_type(request, sheettype):
    if 'q' in request.GET:
        q = request.GET['q']
        sheet = Sheet.objects.filter(title__icontains=q, ) | \
                Sheet.objects.filter(composer__icontains=q, ) | \
                Sheet.objects.filter(type__icontains=q, ) | \
                Sheet.objects.filter(part_of_calender__icontains=q, ) | \
                Sheet.objects.filter(part_of_mass__icontains=q, ) and \
                Sheet.objects.filter(type=sheettype)
        count = sheet.count

        paginator = Paginator(sheet, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)

        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'sheet': sheet,
                   'sheettype': sheettype,
                   'count': count,
                   'about': about,
                   'page_obj': page_obj, }
        return render(request, 'library/sheet_type.html', context)
    else:
        sheet = Sheet.objects.filter(type=sheettype)

        count = sheet.count
        paginator = Paginator(sheet, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)

        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'sheet': sheet,
                   'sheettype': sheettype,
                   'count': count,
                   'about': about,
                   'page_obj': page_obj, }
        return render(request, 'library/sheet_type.html', context)


def getcoverpage(img_name, document, title):
    doc = fitz.open(document)
    count = 0
    for page in doc:
        if count == 1:
            pass
        else:
            count += 1
            pix = page.getPixmap()
            img_name = img_name.replace(' ', '_')
            img_dir = img_name.replace('.pdf', '')
            img_dir = img_dir.replace(' ', '_')
            dir = document.replace('.pdf', '')
            dir = dir.replace(dir[dir.index(img_dir):], '')
            pix.writeImage(f"{img_dir}.png")
            # print(document, '---------------------====', img_dir, '+++', dir)

            original = rf"{img_dir}.png"
            target = rf"{dir}/{img_dir}.png"

            shutil.move(original, target)
            print(document, '---------------------====', img_dir, '+++', dir + '/' + img_dir + '.png')

            saveimg = Sheet.objects.get(title=title)
            saveimg.cover = dir + img_dir + '.png'
            saveimg.save()
            return


@login_required
def viewsheet(request, sheettype, sheetname):
    sheet = Sheet.objects.get(title=sheetname, type=sheettype)
    print(sheet, '=================', sheet.file.url)
    try:
        about = About.objects.get(title='About Madonna Central Choir')
    except Exception:
        about = ''
    context = {'sheet': sheet,
               'abput': about, }
    return render(request, 'library/viewsheet.html', context)


def video(request):
    if 'q' in request.GET:
        q = request.GET['q']
        video = Video.objects.filter(title__icontains=q, ) | \
                Video.objects.filter(composer__icontains=q, ) | \
                Video.objects.filter(type__icontains=q, ) | \
                Video.objects.filter(part_of_calender__icontains=q, ) | \
                Video.objects.filter(part_of_mass__icontains=q, )
        paginator = Paginator(video, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)

        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'video': video,
                   'page_obj': page_obj,
                   'about': about}
        return render(request, 'library/videos.html', context)
    else:
        video = Video.objects.filter()
        paginator = Paginator(video, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)

        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'video': video,
                   'page_obj': page_obj,
                   'about': about}
        return render(request, 'library/videos.html', context)


@login_required
def upload(request, media):
    print('=======================', media)
    if request.user.is_staff:
        if request.method == 'GET':
            try:
                about = About.objects.get(title='About Madonna Central Choir')
            except Exception:
                about = ''
            context = {'media': media,
                       'about': about}
            return render(request, 'library/upload.html', context)

        elif request.method == 'POST':
            title = request.POST['title']
            composer = request.POST['composer']
            type = request.POST['type']
            part_of_calender = request.POST['part_of_calender']
            part_of_mass = request.POST['part_of_mass']

            file = request.FILES['file']
            shcount = 1
            media_ = ''
            if media == 'Video':
                media_ = Video.objects.filter(title=title)
            elif media == 'Audio':
                media_ = Audio.objects.filter(title=title)
                print(media)
            elif media == 'Sheet':
                media_ = Sheet.objects.filter(title=title)

            if media_.exists():
                shcount = 0
                messages.warning(request, f'A {media} with title "{title}" already exists')

                try:
                    about = About.objects.get(title='About Madonna Central Choir')
                except Exception:
                    about = ''
                context = {'values': request.POST,
                           'valfile': request.FILES,
                           'invalid': shcount,
                           'about': about, }
                return redirect('upload')
            if media == 'Video':
                try:
                    instance = Video(title=title, composer=composer,
                                     type=type, part_of_calender=part_of_calender,
                                     part_of_mass=part_of_mass,
                                     uploader=request.user, file=file)
                    instance.save()
                except Exception:
                    pass
            elif media == 'Audio':
                try:
                    instance = Audio(title=title, composer=composer,
                                     type=type, part_of_calender=part_of_calender,
                                     part_of_mass=part_of_mass,
                                     uploader=request.user, file=file)
                    instance.save()
                except Exception:
                    pass
            elif media == 'Sheet':
                try:
                    instance = Sheet(title=title, composer=composer, cover='cover',
                                     type=type, part_of_calender=part_of_calender,
                                     part_of_mass=part_of_mass, uploader=request.user,
                                     file=file)
                    instance.save()

                    cover_page = Sheet.objects.get(title=title)
                    a = os.path.abspath(str(cover_page.file))
                    a = a.replace(a[a.index('Documents'):], '')
                    a = a + 'media/' + str(cover_page.file)
                    img_name = str(file)
                    # print(cover_page.file, '====', a)
                    cover = getcoverpage(img_name, a, title)
                except Exception:
                    pass

            messages.success(request, f'The {media} has been added successfully')
            return redirect('upload', media)
    else:
        messages.error(request, 'Invalid Url')
        next = request.META['HTTP_REFERER']
        return HttpResponseRedirect(next)


def audio(request):
    if 'q' in request.GET:
        q = request.GET['q']
        audio = Audio.objects.filter(title__icontains=q, ) | \
                Audio.objects.filter(composer__icontains=q, ) | \
                Audio.objects.filter(type__icontains=q, ) | \
                Audio.objects.filter(part_of_calender__icontains=q, ) | \
                Audio.objects.filter(part_of_mass__icontains=q, )
        paginator = Paginator(audio, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)

        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'audio': audio,
                   'page_obj': page_obj,
                   'about': about, }
        return render(request, 'library/audio.html', context)
    else:
        audio = Audio.objects.filter()
        paginator = Paginator(audio, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)

        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'audio': audio,
                   'page_obj': page_obj,
                   'about': about, }
        return render(request, 'library/audio.html', context)


@login_required
def viewaudio(request, audioname):
    print('audionm------------', audioname)
    audio = Audio.objects.get(title=audioname)
    try:
        about = About.objects.get(title='About Madonna Central Choir')
    except Exception:
        about = ''
    context = {'audio': audio,
               'about': about}
    return render(request, 'library/viewaudio.html', context)


def document(request):
    if 'q' in request.GET:
        q = request.GET['q']
        doc = Document.objects.filter(title__icontains=q, )
        paginator = Paginator(doc, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'doc': doc,
                   'page_obj': page_obj,
                   'about': about}
        return render(request, 'library/documents.html', context)
    else:
        doc = Document.objects.filter()
        paginator = Paginator(doc, 12)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'doc': doc,
                   'page_obj': page_obj,
                   'about': about}
        return render(request, 'library/documents.html', context)


@login_required
def viewdoc(request, title):
    doc = Document.objects.get(title=title)
    try:
        about = About.objects.get(title='About Madonna Central Choir')
    except Exception:
        about = ''
    context = {'doc': doc,
               'about': about}
    return render(request, 'library/viewdoc.html', context)


@login_required
def uploaddoc(request, docname):
    if request.method == 'GET':
        try:
            about = About.objects.get(title='About Madonna Central Choir')
        except Exception:
            about = ''
        context = {'values': request.POST,
                   'docname': docname,
                   'about': about, }
        return render(request, 'library/uploaddoc.html', context)

    elif request.method == 'POST':
        title = request.POST['title']
        details = request.POST['details']
        campus = request.POST['campus']
        file = request.FILES['file']
        doc = Document.objects.filter(title=title, )
        if doc.exists():
            shcount = 0
            messages.warning(request, f'A {docname} with title "{title}" already exists')

            try:
                about = About.objects.get(title='About Madonna Central Choir')
            except Exception:
                about = ''
            context = {'values': request.POST,
                       'valfile': request.FILES,
                       'invalid': shcount,
                       'about': about, }
            return redirect('upload', docname)
        print('dfgfdgdfgdfgdfgdfg======')
        try:
            instance = Document(title=title, details=details, campus=Campus.objects.get(campus=campus),
                                uploader=request.user, file=file)
            instance.save()
        except Exception:
            pass

        messages.success(request, f'The {docname} has been added successfully')
        return redirect('uploaddoc', docname)
