import Layout from "@/layout"

const goodsizeRouter = {
    path: "/goodsize",
    name: "goodsize",
    redirect: "/goodsize/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/goodsize/index"),
        meta: { title: "商品尺码管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/goodsize/edit"),
        hidden: true,
        meta: { title: "修改商品尺码" }
    },
    {
        path: "add",
        component: () => import("@/views/goodsize/add"),
        hidden: true,
        meta: { title: "添加商品尺码" }
    }
    ]
}

export default goodsizeRouter