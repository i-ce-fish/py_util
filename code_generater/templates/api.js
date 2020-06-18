import request from "@/utils/request"


export function get{{ModelNamePlural|title}}(params) {
    return request({
        url: "/api/{{ModelNamePlural}}",
        method: "get",
        params
    })
}

export function get{{ModelNameSingular|title}}(id) {
    return request({
        url: `/api/{{ModelNamePlural}}/${id}`,
        method: "get"
    })
}

export function add{{ModelNameSingular|title}}(data) {
    return request({
        url: "/api/{{ModelNamePlural}}",
        method: "post",
        data
    })
}

export function put{{ModelNameSingular|title}}(id, data) {
    return request({
        url: `/api/{{ModelNamePlural}}/${id}`,
        method: "put",
        data
    })
}

export function del{{ModelNameSingular|title}}(id) {
    return request({
        url: `/api/{{ModelNamePlural}}/${id}`,
        method: "delete"
    })
}
