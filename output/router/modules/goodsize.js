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
        meta: { title: "尺码表管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/goodsize/edit"),
        hidden: true,
        meta: { title: "修改尺码表" }
    },
    {
        path: "add",
        component: () => import("@/views/goodsize/add"),
        hidden: true,
        meta: { title: "添加尺码表" }
    }
    ]
}

export default goodsizeRouter