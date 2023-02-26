function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$('#cities').focus(function(){
    $('.city-select__list').fadeIn()
})

$('#cities').blur(function(){
    $('.city-select__list').fadeOut()
})

function displayList({ cities }){
    list = $('.city-select__list')
    list.empty()
    cities.map(value => {
        city = value.name
        region = value.region__name ? value.region__name + ', ': ''
        country = value.country__name
        list.append(`
            <div  class='city-select__item'> ${city}, ${region} ${country}
        `)
    })
}

$('select[name="country"]').on('change', function(){
    country = $(this).find('option:selected').text()
    $.ajax({
        method: "POST",
        url: '/orders/ajax/cities/',
        headers: { "X-CSRFToken": getCookie("csrftoken")},
        data: {country: country},
        success: displayList
    })
})

$('#cities').on('input', function(){
    text = $(this).val()
    country = $('select[name="country"] option:selected').text()
    $.ajax({
        method: "PUT",
        url: '/orders/ajax/cities/',
        headers: { "X-CSRFToken": getCookie("csrftoken")},
        data: {country: country, city: text},
        success: displayList
    })
})

$(document).on('click', '.city-select__item', function(){
    text = $(this).text()
    $('#cities').val(text)
})