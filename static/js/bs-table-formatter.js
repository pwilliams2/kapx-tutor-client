/**
 * Created by admin on 1/12/15.
 */

    function statusFormatter(value, row) {
        var isAvailable = (row.status == 'Available') ? true : false;

        if (isAvailable)
           return statusUI = '<b style="color:green">' + value + '</b>&nbsp;&nbsp;&nbsp;&nbsp;'
               + '<button type="submit" class="btn btn-success btn-xs" aria-label="Left Align">'
               + '<span class="glyphicon glyphicon-facetime-video" aria-hidden="true"></span></button>'
               + '</button>';
        else
            return value;
        //return '<i class="glyphicon ' + icon + '"></i> ' + value;
    }

    function priceFormatter(value) {
        // 16777215 == ffffff in decimal
        var color = '#'+Math.floor(Math.random() * 6777215).toString(16);
        return '<div  style="color: ' + color + '">' +
                '<i class="glyphicon glyphicon-usd"></i>' +
                value.substring(1) +
                '</div>';
    }
