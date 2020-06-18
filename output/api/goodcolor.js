import request from "@/utils/request"


export function getGoodcolors(params) {
    return request({
        url: "/api/goodcolors",
        method: "get",
        params
    })
}

export function getGoodcolor(id) {
    return request({
        url: `/api/goodcolors/${id}`,
        method: "get"
    })
}

export function addGoodcolor(data) {
    return request({
        url: "/api/goodcolors",
        method: "post",
        data
    })
}

export function putGoodcolor(id, data) {
    return request({
        url: `/api/goodcolors/${id}`,
        method: "put",
        data
    })
}

export function delGoodcolor(id) {
    return request({
        url: `/api/goodcolors/${id}`,
        method: "delete"
    })
}