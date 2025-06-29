/*
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
 
 https://github.com/delthia/bus-coruna-api

 */
// Service worker para instalar la PWA, y que hace funcionar la caché en la misma
self.addEventListener("install", event => {
    console.log("Service worker installed");
});
self.addEventListener("activate", event => {
    console.log("Service worker activated");    
})

caches.open("pwa-assets")
.then(cache => {
    cache.addAll(["/","/static/css/main.css",
        "/static/icons/icon-256.png",
        "/static/icons/icon-512.png",
        "/static/fonts/roboto-bold.woff2",
        "/static/fonts/roboto-regular.woff2"]);
})

 self.addEventListener("fetch", event => {
    event.respondWith(
      fetch(event.request)
      .catch(error => {
        return caches.match(event.request) ;
      })
    );
 });