package com.netease.edu.utest;

import org.springframework.test.annotation.Rollback;
import org.springframework.test.context.TestExecutionListeners;
import org.springframework.test.context.support.DependencyInjectionTestExecutionListener;
import org.springframework.test.context.testng.AbstractTestNGSpringContextTests;

import com.netease.edu.utest.listener.CacheClearListener;
import com.netease.edu.utest.listener.DBRollbackListener;
import com.netease.edu.utest.listener.MockListener;

/**
 * Created by hzfjd on 16/9/8.
 */
@TestExecutionListeners({DependencyInjectionTestExecutionListener.class, DBRollbackListener.class, MockListener.class, CacheClearListener.class})
@Rollback
public class BaseTestNg extends AbstractTestNGSpringContextTests{

}
