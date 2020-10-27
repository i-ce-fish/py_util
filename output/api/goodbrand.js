import request from "@/utils/request"


export function getGoodbrands(params) {
    return request({
        url: "/api/goodbrands",
        method: "get",
        params
    })
}

export function getGoodbrand(id) {
    return request({
        url: `/api/goodbrands/${id}`,
        method: "get"
    })
}

export function addGoodbrand(data) {
    return request({
        url: "/api/goodbrands",
        method: "post",
        data
    })
}

export function putGoodbrand(id, data) {
    return request({
        url: `/api/goodbrands/${id}`,
        method: "put",
        data
    })
}

export function delGoodbrand(id) {
    return request({
        url: `/api/goodbrands/${id}`,
        method: "delete"
    })
}