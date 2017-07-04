$(document).ready(function () {

    $.ajax({
        url: 'json/connected',
    }).done(function (data) {
        // Si Json renvoi true, le user est connecté : on affiche le bouton déconnexion
        if (data.success) {
            $('#logout').show();
            $('#login').hide();
        }
        // Si Json renvoi false, le user n'est pas connecté : on affiche le formulaire de connexion
        else {
            $('#logout').hide();
            $('#login').show();
        }
    })


    $('#logout').submit(function () {
        // Récupération url
        var url = $(this).attr('action');

        // Appel ajax
        $.ajax({
            url: url,
            method: $(this).attr('method'),
            data: $(this).serialize()
        }).done(function (data) {
            window.location.reload(true);
        }).error(function () {
            alert("Erreur crtique !")
        });
        // Fin ajax

        return false; // Fait croire que le formulaire a eu un problème, et donc ne l'envoi pas
    })


    $('#login').submit(function () {
        // Récupération url
        var url = $(this).attr('action');

        // Appel ajax
        $.ajax({
            url: url,
            method: $(this).attr('method'),
            data: $(this).serialize()
        }).done(function (data) {
            if (data.success) {
                window.location.reload(true);
            }
            //data.message
        }).error(function () {
            alert("Erreur crtique !")
        });
        // Fin ajax

        return false; // Fait croire que le formulaire a eu un problème, et donc ne l'envoi pas
    })


    /* ======= Fixed header when scrolled ======= */
    $(window).bind('scroll', function () {
        if ($(window).scrollTop() > 0) {
            $('#header').addClass('header-scrolled');
        }
        else {
            $('#header').removeClass('header-scrolled');
        }
    });

    /* ======= Scrollspy ======= */
    $('body').scrollspy({target: '#header', offset: 100});

    /* ======= ScrollTo ======= */
    $('a.scrollto').on('click', function (e) {

        //store hash
        var target = this.hash;

        e.preventDefault();

        $('body').scrollTo(target, 800, {offset: -50, 'axis': 'y'});
        //Collapse mobile menu after clicking
        if ($('.navbar-collapse').hasClass('in')) {
            $('.navbar-collapse').removeClass('in').addClass('collapse');
        }

    });

});