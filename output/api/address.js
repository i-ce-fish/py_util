import request from "@/utils/request"


export function getAddresses(params) {
    return request({
        url: "/api/addresses",
        method: "get",
        params
    })
}

export function getAddress(id) {
    return request({
        url: `/api/addresses/${id}`,
        method: "get"
    })
}

export function addAddress(data) {
    return request({
        url: "/api/addresses",
        method: "post",
        data
    })
}

export function putAddress(id, data) {
    return request({
        url: `/api/addresses/${id}`,
        method: "put",
        data
    })
}

export function delAddress(id) {
    return request({
        url: `/api/addresses/${id}`,
        method: "delete"
    })
}