import request from "@/utils/request"


export function getCustomers(params) {
    return request({
        url: "/api/customers",
        method: "get",
        params
    })
}

export function getCustomer(id) {
    return request({
        url: `/api/customers/${id}`,
        method: "get"
    })
}

export function addCustomer(data) {
    return request({
        url: "/api/customers",
        method: "post",
        data
    })
}

export function putCustomer(id, data) {
    return request({
        url: `/api/customers/${id}`,
        method: "put",
        data
    })
}

export function delCustomer(id) {
    return request({
        url: `/api/customers/${id}`,
        method: "delete"
    })
}