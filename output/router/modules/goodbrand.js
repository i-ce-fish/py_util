import Layout from "@/layout"

const goodbrandRouter = {
    path: "/goodbrand",
    name: "goodbrand",
    redirect: "/goodbrand/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/goodbrand/index"),
        meta: { title: "品牌名称管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/goodbrand/edit"),
        hidden: true,
        meta: { title: "修改品牌名称" }
    },
    {
        path: "add",
        component: () => import("@/views/goodbrand/add"),
        hidden: true,
        meta: { title: "添加品牌名称" }
    }
    ]
}

export default goodbrandRouter