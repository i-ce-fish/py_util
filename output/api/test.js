import request from "@/utils/request"


export function getTests(params) {
    return request({
        url: "/api/tests",
        method: "get",
        params
    })
}

export function getTest(id) {
    return request({
        url: `/api/tests/${id}`,
        method: "get"
    })
}

export function addTest(data) {
    return request({
        url: "/api/tests",
        method: "post",
        data
    })
}

export function putTest(id, data) {
    return request({
        url: `/api/tests/${id}`,
        method: "put",
        data
    })
}

export function delTest(id) {
    return request({
        url: `/api/tests/${id}`,
        method: "delete"
    })
}