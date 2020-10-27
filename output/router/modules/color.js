import Layout from "@/layout"

const colorRouter = {
    path: "/color",
    name: "color",
    redirect: "/color/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/color/index"),
        meta: { title: "颜色管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/color/edit"),
        hidden: true,
        meta: { title: "修改颜色" }
    },
    {
        path: "add",
        component: () => import("@/views/color/add"),
        hidden: true,
        meta: { title: "添加颜色" }
    }
    ]
}

export default colorRouter