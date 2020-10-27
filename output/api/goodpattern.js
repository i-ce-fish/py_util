import request from "@/utils/request"


export function getGoodpatterns(params) {
    return request({
        url: "/api/goodpatterns",
        method: "get",
        params
    })
}

export function getGoodpattern(id) {
    return request({
        url: `/api/goodpatterns/${id}`,
        method: "get"
    })
}

export function addGoodpattern(data) {
    return request({
        url: "/api/goodpatterns",
        method: "post",
        data
    })
}

export function putGoodpattern(id, data) {
    return request({
        url: `/api/goodpatterns/${id}`,
        method: "put",
        data
    })
}

export function delGoodpattern(id) {
    return request({
        url: `/api/goodpatterns/${id}`,
        method: "delete"
    })
}