import request from "@/utils/request"


export function getSupplies(params) {
    return request({
        url: "/api/supplies",
        method: "get",
        params
    })
}

export function getSupply(id) {
    return request({
        url: `/api/supplies/${id}`,
        method: "get"
    })
}

export function addSupply(data) {
    return request({
        url: "/api/supplies",
        method: "post",
        data
    })
}

export function putSupply(id, data) {
    return request({
        url: `/api/supplies/${id}`,
        method: "put",
        data
    })
}

export function delSupply(id) {
    return request({
        url: `/api/supplies/${id}`,
        method: "delete"
    })
}