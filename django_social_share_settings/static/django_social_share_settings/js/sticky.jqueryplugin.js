/*!
 * author:nina@cgpartnersllc.com
 * Provides simple sticky functionality
 */


// the semi-colon before the function invocation is a safety
// net against concatenated scripts and/or other plugins
// that are not closed properly.
;(function ( $, window, document, undefined ) {

    // undefined is used here as the undefined global
    // variable in ECMAScript 3 and is mutable (i.e. it can
    // be changed by someone else). undefined isn't really
    // being passed in so we can ensure that its value is
    // truly undefined. In ES5, undefined can no longer be
    // modified.

    // window and document are passed through as local
    // variables rather than as globals, because this (slightly)
    // quickens the resolution process and can be more
    // efficiently minified (especially when both are
    // regularly referenced in your plugin).

    // Create the defaults once
    var pluginName = "sticky",
        defaults = {
            topSelector : "#main",
            bottomSelector : "#footer",
            fixedMargin : 0,
            topMargin : 0,
            bottomMargin : 0,
            unitScaler: 1
        };

    // The actual plugin constructor
    function Sticky( element, options ) {
        this.element = element;

        // jQuery has an extend method that merges the
        // contents of two or more objects, storing the
        // result in the first object. The first object
        // is generally empty because we don't want to alter
        // the default options for future instances of the plugin
        this.options = $.extend( {}, defaults, options) ;

        if($(this.options.topSelector).length <= 0 ||  $(this.options.bottomSelector).length <= 0){
            //console.log("missing pieces.")
            return;
        }

        this._defaults = defaults;
        this._name = pluginName;

        this.winw = $(window).width(),
        this.winh = $(window).height();

        this.init();

        

        //Note -- jquery ready doesn't execute at the correct time for old ies
        //So let's manually update this.
        var parent = this;
        if( $(".ie8,.ie7,.ie6").length > 0){
            setTimeout(function(){
                parent.updateMeasurements();
                parent.render();
            },500);
        }

        $( "img" ).load(function() {
            parent.updateMeasurements();
            parent.render();
        });
        setTimeout(function(){
            parent.updateMeasurements();
            parent.render();
        },5);
        


        
    }

    Sticky.prototype = {

        init: function() {
            // Place initialization logic here
            // You already have access to the DOM element and
            // the options via the instance, e.g. this.element
            // and this.options
            // you can add more functions like the one below and
            // call them like so: this.yourOtherFunction(this.element, this.options).
            //console.log("topSelector? "+this.options.topSelector)
            

            this.updateMeasurements();

            this.addListeners()
          

            this.render()

            $(this.element).addClass("inited");
        },
       
        updateMeasurements: function(){
            this.socialWidgetHeight = $(this.element).outerHeight();
            this.mainTopPosition = this.getElementPosition(this.options.topSelector);
            this.footerTopPosition = $(this.options.bottomSelector).offset().top;
            
            var staticTopUnscaled = (this.mainTopPosition) - $(window).scrollTop();
            var staticBottomUnscaled = (this.footerTopPosition) - $(window).scrollTop();
            this.staticTop =  staticTopUnscaled / this.options.unitScaler;
            this.staticBottom =  staticBottomUnscaled / this.options.unitScaler;
            
            //console.log("mainTopPosition: "+this.mainTopPosition+" staticTop: "+this.staticTop+" unscaled: "+staticTopUnscaled);
            //console.log("footerTopPosition: "+this.footerTopPosition+" staticBottom: "+this.staticBottom+" unscaled: "+staticBottomUnscaled);

            if($(".ie11").length > 0){
                this.staticTop = this.staticTop + 16;
            }           

        },
        getElementPosition: function(element){
            return $(element).offset().top + parseInt($(this.options.topSelector).css('padding-top'));// + parseInt($(this.options.topSelector).css('padding-bottom'))
        },
        render: function() {
          //Update view

            var fixedMargin = this.options.fixedMargin;
            var topMargin = this.options.topMargin;
            var bottomMargin = this.options.bottomMargin;
        


            var scrollTop = $(window).scrollTop();
            var windowHeight = $(window).height();
            var scrollPosition = scrollTop;

            var fixedPosition = fixedMargin;

            var topMax = this.staticTop - fixedMargin;
            var bottomMax = ((this.socialWidgetHeight + bottomMargin) / this.options.unitScaler) + fixedMargin;
            var stickToBottomPosition = (this.footerTopPosition / this.options.unitScaler) - (this.socialWidgetHeight) - (bottomMargin);
            
            if (this.staticBottom < bottomMax ) {
                //console.log("stick to bottom");

                $(this.element).css("top", stickToBottomPosition);
                $(this.element).addClass("sticking");

            } else if (this.staticTop+topMargin < fixedMargin) {
                //console.log("fixed");

                $(this.element).css("top", fixedPosition);
                
                $(this.element).removeClass("sticking")
            }else {
                //console.log("stick to top")
                
                $(this.element).css("top", this.options.topMargin+'px');
                $(this.element).addClass("sticking")
            }
            
            //console.log("topSelector: "+this.options.topSelector+" scrollTop: "+scrollTop+" fixedMargin: "+fixedMargin+" topMax: "+topMax+" bottomMax: "+bottomMax);

            
        },

        addListeners: function() {
            //bind events
            var parent = this;
            $(window).bind("scroll", function(){
                parent.updateMeasurements();
                parent.render();
            }); 
            $(window).unbind("touchmove", function(){
                parent.render();
            }); 
            $(window).bind("resize", function(){
                if( $(window).width()!= parent.winw || $(window).height()!= parent.winh ){
                    parent.winw = $(window).width(),
                    parent.winh = $(window).height();
                    parent.updateMeasurements();
                    parent.render();
                }
               
            }); 
        },

        removeListeners: function() {
            //unbind events          
            $(window).unbind("scroll", function(){
                parent.updateMeasurements();
                parent.render();
            }); 
            $(window).unbind("resize", function(){
                parent.updateMeasurements();
                parent.render();
            });  
        }

    };

    // A really lightweight plugin wrapper around the constructor,
    // preventing against multiple instantiations
    $.fn[pluginName] = function ( options ) {
        return this.each(function () {
            if (!$.data(this, "plugin_" + pluginName)) {
                $.data(this, "plugin_" + pluginName,
                new Sticky( this, options ));
            }
        });
    };

})( jQuery, window, document );