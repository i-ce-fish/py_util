import Layout from "@/layout"

const color2Router = {
    path: "/color2",
    name: "color2",
    redirect: "/color2/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/color2/index"),
        meta: { title: "颜色名称管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/color2/edit"),
        hidden: true,
        meta: { title: "修改颜色名称" }
    },
    {
        path: "add",
        component: () => import("@/views/color2/add"),
        hidden: true,
        meta: { title: "添加颜色名称" }
    }
    ]
}

export default color2Router