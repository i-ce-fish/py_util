import Layout from "@/layout"

const goodcolorRouter = {
    path: "/goodcolor",
    name: "goodcolor",
    redirect: "/goodcolor/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/goodcolor/index"),
        meta: { title: "服装颜色表管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/goodcolor/edit"),
        hidden: true,
        meta: { title: "修改服装颜色表" }
    },
    {
        path: "add",
        component: () => import("@/views/goodcolor/add"),
        hidden: true,
        meta: { title: "添加服装颜色表" }
    }
    ]
}

export default goodcolorRouter