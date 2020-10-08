import Layout from "@/layout"

const testRouter = {
    path: "/test",
    name: "test",
    redirect: "/test/index",
    component: Layout,
    children: [{
        path: "index",
        name: "index",
        component: () => import("@/views/test/index"),
        meta: { title: "测试模板管理", icon: "tree" }
    }, {
        path: "edit",
        component: () => import("@/views/test/edit"),
        hidden: true,
        meta: { title: "修改测试模板" }
    },
    {
        path: "add",
        component: () => import("@/views/test/add"),
        hidden: true,
        meta: { title: "添加测试模板" }
    }
    ]
}

export default testRouter