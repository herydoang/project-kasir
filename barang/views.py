from django.shortcuts import render, redirect
from barang.models import *

def barang_list(request):
    template_name = 'barang_list.html'
    produk_list = Produk.objects.all()
    context = {
        'title' : 'List Barang',
        'produk' : produk_list,
    }    
    return render(request, template_name, context)

def barang_add(request):
    template_name = 'barang_add.html'
    kategori = Kategori.objects.all() 
    if request.method == "POST":
        input_kategori = request.POST.get('kategori')
        input_nama = request.POST.get('nama')
        input_deskripsi = request.POST.get('deskripsi')
        input_jumlah = request.POST.get('jumlah')

        #panggil kategori
        get_kategori = Kategori.objects.get(nama=input_kategori)

        #simpan produk
        Produk.objects.create(
            nama = input_nama,
            deskripsi = input_deskripsi,
            jumlah = input_jumlah,
            kategori = get_kategori,
        )
        return redirect(barang_list)
    context = {
        'title' : 'Tambah Barang',
        'kategori' : kategori,
    }
    return render(request, template_name, context)

#function edit data
def barang_update(request, id):
    template_name = 'barang_add.html'
    kategori = Kategori.objects.all()
    get_produk = Produk.objects.get(id=id)

    if request.method == "POST" :

        input_kategori  = request.POST.get('kategori')
        input_nama      = request.POST.get('nama')
        input_deskripsi = request.POST.get('deskripsi')
        input_jumlah    = request.POST.get('jumlah')

        # memanggil kategori
        get_kategori = Kategori.objects.get(nama=input_kategori)

        # menyimpan produk
        get_produk.nama = input_nama
        get_produk.deskripsi = input_deskripsi
        get_produk.jumlah = input_jumlah
        get_produk.kategori = get_kategori
        get_produk.save()
        return  redirect(barang_list)
    context = {
        'title'     : 'Update Barang',
        'kategori'  : kategori,
        'get_produk': get_produk,
    }
    return render(request, template_name, context)

#function hapus data
def barang_delete(request, id ):
    Produk.objects.get(id=id).delete()
    return  redirect(barang_list)



