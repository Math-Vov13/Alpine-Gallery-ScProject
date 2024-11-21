# Schema de l'API

Les différents endpoints avec les bonnes méthodes et les body attendus sont affichés ici !


Account

```js
POST api/v1/account/register
{
    name = ''
    email = ''
    password = ''
}
```

```js
POST api/v1/account/login
{
    email = ''
    password = ''
}
```


Files Management

```js
GET api/v1/gallery
```

```js
GET api/v1/gallery/{media_id}
```

```js
POST api/v1/gallery
{
    FILE: FILE
}
```

```js
DELETE api/v1/gallery/{media_id}
```