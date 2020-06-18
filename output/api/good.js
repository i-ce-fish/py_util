import request from "@/utils/request"


export function getGoods(params) {
    return request({
        url: "/api/goods",
        method: "get",
        params
    })
}

export function getGood(id) {
    return request({
        url: `/api/goods/${id}`,
        method: "get"
    })
}

export function addGood(data) {
    return request({
        url: "/api/goods",
        method: "post",
        data
    })
}

export function putGood(id, data) {
    return request({
        url: `/api/goods/${id}`,
        method: "put",
        data
    })
}

export function delGood(id) {
    return request({
        url: `/api/goods/${id}`,
        method: "delete"
    })
}