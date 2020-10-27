import request from "@/utils/request"


export function getSupplierorders(params) {
    return request({
        url: "/api/supplierorders",
        method: "get",
        params
    })
}

export function getSupplierorder(id) {
    return request({
        url: `/api/supplierorders/${id}`,
        method: "get"
    })
}

export function addSupplierorder(data) {
    return request({
        url: "/api/supplierorders",
        method: "post",
        data
    })
}

export function putSupplierorder(id, data) {
    return request({
        url: `/api/supplierorders/${id}`,
        method: "put",
        data
    })
}

export function delSupplierorder(id) {
    return request({
        url: `/api/supplierorders/${id}`,
        method: "delete"
    })
}