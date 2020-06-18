import request from "@/utils/request"


export function getOrderitems(params) {
    return request({
        url: "/api/orderitems",
        method: "get",
        params
    })
}

export function getOrderitem(id) {
    return request({
        url: `/api/orderitems/${id}`,
        method: "get"
    })
}

export function addOrderitem(data) {
    return request({
        url: "/api/orderitems",
        method: "post",
        data
    })
}

export function putOrderitem(id, data) {
    return request({
        url: `/api/orderitems/${id}`,
        method: "put",
        data
    })
}

export function delOrderitem(id) {
    return request({
        url: `/api/orderitems/${id}`,
        method: "delete"
    })
}