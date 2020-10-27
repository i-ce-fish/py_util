import request from "@/utils/request"


export function getGoodtextures(params) {
    return request({
        url: "/api/goodtextures",
        method: "get",
        params
    })
}

export function getGoodtexture(id) {
    return request({
        url: `/api/goodtextures/${id}`,
        method: "get"
    })
}

export function addGoodtexture(data) {
    return request({
        url: "/api/goodtextures",
        method: "post",
        data
    })
}

export function putGoodtexture(id, data) {
    return request({
        url: `/api/goodtextures/${id}`,
        method: "put",
        data
    })
}

export function delGoodtexture(id) {
    return request({
        url: `/api/goodtextures/${id}`,
        method: "delete"
    })
}