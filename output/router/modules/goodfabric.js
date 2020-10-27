import Layout from "@/layout"

const goodfabricRouter = {
    path: "/goodfabric",
    name: "goodfabric",
    redirect: "/goodfabric/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/goodfabric/index"),
        meta: { title: "面料名称管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/goodfabric/edit"),
        hidden: true,
        meta: { title: "修改面料名称" }
    },
    {
        path: "add",
        component: () => import("@/views/goodfabric/add"),
        hidden: true,
        meta: { title: "添加面料名称" }
    }
    ]
}

export default goodfabricRouter