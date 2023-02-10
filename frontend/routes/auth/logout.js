const express = require('express');

const cookie = require('cookie');


const router = express.Router();

router.get('/api/users/logout/', (req, res)=> {
    res.setHeader('Set-Cookie', [
        cookie.serializer('access', '', {
            httpOnly: true,
            expired: new Date(0),
            path: "/api/",
            sameSite: "strict",
            secure: process.env.NODE_ENV === 'production'
        }),
        cookie.serializer('refresh', '', {
            httpOnly: true,
            expired: new Date(0),
            path: "/api/",
            sameSite: "strict",
            secure: process.env.NODE_ENV === 'production'
        }),
    ])

    return res.status(200).json({ sucess: 'Logour success'});
})

module.exports = router;