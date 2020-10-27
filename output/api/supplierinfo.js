import request from "@/utils/request"


export function getSupplierinfos(params) {
    return request({
        url: "/api/supplierinfos",
        method: "get",
        params
    })
}

export function getSupplierinfo(id) {
    return request({
        url: `/api/supplierinfos/${id}`,
        method: "get"
    })
}

export function addSupplierinfo(data) {
    return request({
        url: "/api/supplierinfos",
        method: "post",
        data
    })
}

export function putSupplierinfo(id, data) {
    return request({
        url: `/api/supplierinfos/${id}`,
        method: "put",
        data
    })
}

export function delSupplierinfo(id) {
    return request({
        url: `/api/supplierinfos/${id}`,
        method: "delete"
    })
}