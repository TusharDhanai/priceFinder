// Javascript to insert company icons on the select box options in the track page.
// I don't understand how this actually works, all I know is that I give some options and jquery-ui handles
// the rest.
$(function() {
    $.widget( "custom.iconselectmenu", $.ui.selectmenu, {
        options: {
            classes: {
                "ui-selectmenu-button": "form-control",
                "ui-selectmenu-icon": 'mt-1'
            },
            width: '100%',
        },
        _renderItem: function( ul, item ) {
          var li = $( "<li>" ),
            wrapper = $( "<div>", { text: item.label } );
   
          if ( item.disabled ) {
            li.addClass( "ui-state-disabled" );
          }

            // $( "<span>", {
            //     style: item.element.attr( "data-style" ),
            //     "class": "ui-icon " + item.element.attr( "data-class" )
            // })
            $( "<span>", {
                html:"&emsp;&emsp;",
                style: `width:50px; height: 24px; top:0.1em; 
                        background: url('static/assets/img/brand/${item.element.attr('data-image')}') no-repeat;
                        background-size: 20px;`,   // use style and set background image
            }).prependTo( wrapper );
   
            return li.append( wrapper ).appendTo( ul );
        }
      });

      $( "#platform" )
      .iconselectmenu()
      .iconselectmenu( "menuWidget" )
        .addClass( "ui-menu-icons" );
})