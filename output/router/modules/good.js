import Layout from "@/layout"

const goodRouter = {
    path: "/good",
    name: "good",
    redirect: "/good/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/good/index"),
        meta: { title: "商品模块管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/good/edit"),
        hidden: true,
        meta: { title: "修改商品模块" }
    },
    {
        path: "add",
        component: () => import("@/views/good/add"),
        hidden: true,
        meta: { title: "添加商品模块" }
    }
    ]
}

export default goodRouter