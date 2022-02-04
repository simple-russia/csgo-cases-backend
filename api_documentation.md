# 📋 Documentation for the server API
<!-- <br></br> -->
## 1. Get all the cases available
### https://example.com/api/get-all-cases/
Returns a JSON with data about all the available cases.

Response example:
```JS
[
    {
        id: 1,
        name: "Winter Offensive",
        price: 80.00,
        imageurl: "/cases/winter_offensive.png",
        is_special: "1",
    },
    {
        id: 2,
        name: "Mirage",
        price: 45.00,
        imageurl: "/cases/mirage.png",
        is_special: "0",
    },
    ...
]
```
<br></br>
## 2. Get all the weapons related to the case
### https://example.com/api/get-weapons?case=`case_id`
Returns a JSON with the list of weapons that are available in the chosen case + the info about the case itself

Response example:
```JS
{   
    case: {
        id: 1,
        name: "Winter Offensive",
        price: 80.00,
        imageurl: "/cases/winter_offensive.png",
        is_special: "0",
    },

    weapons: [
        {
            id: 1,
            style: "azimov",
            type: "M4A4",
            price: 140.00,
            color: "red",
            imageurl: "/weapons/m4a4-azimov.png/",
            collection: "Winter Offensive",
            stattrak: 1, // 1 = can be stattrak, 2 = cannot
        },
        ...
    ],
}
```
<br></br>
## 3. Get a few certain weapons
### https://example.com/api/get-weapons/
The query is sent with `request.body` that contains JSON array of the few weapons to be returned

request.body example
`[1, 2, 5, 6, 9, 11, 12, 56, 57]`

Response example:
```JS
[
    {
        id: 1,
        style: "azimov",
        type: "M4A4",
        price: 140.00,
        color: "red",
        imageurl: "/weapons/m4a4-azimov.png/",
        collection: "Winter Offensive",
        stattrak: 1, // 1 = can be stattrak, 2 = cannot
    },
    ...
]
```
<br></br>
## 4. Get all the weapons related to some collection
### https://example.com/api/get-weapons?collection=`collection_id`

Returns a JSON with the list of weapons that belong to the chosen collection

Response example:
```JS
[
    {
        id: 1,
        style: "azimov",
        type: "M4A4",
        price: 140.00,
        color: "red",
        imageurl: "/weapons/m4a4-azimov.png/",
        collection: "Winter Offensive",
        stattrak: 1, // 1 = can be stattrak, 2 = cannot
    },
    ...
]
```



