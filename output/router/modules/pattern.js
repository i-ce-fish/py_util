import Layout from "@/layout"

const patternRouter = {
    path: "/pattern",
    name: "pattern",
    redirect: "/pattern/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/pattern/index"),
        meta: { title: "图案管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/pattern/edit"),
        hidden: true,
        meta: { title: "修改图案" }
    },
    {
        path: "add",
        component: () => import("@/views/pattern/add"),
        hidden: true,
        meta: { title: "添加图案" }
    }
    ]
}

export default patternRouter